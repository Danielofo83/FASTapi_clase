from datetime import datetime, timedelta, timezone  
from typing import List, Optional
import jwt
from pwdlib import PasswordHash
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

#pip install pyjwt crypto
#pip install pwdlib 

SECRET KEY = "super_cadena_de_caracteres_plus_ultra_para_jwt_seguros_2026_20_30_si"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title = "API de Autenticación con JWT y FastAPI", version = "1.0.0")

class UsuarioBase(BaseModel):
    username: str = Field(..., example="usuario1")
    password: str = Field(..., example="contraseña123")

class UsuarioEnDB(UsuarioBase):
    hashed_password: str
    disabled: bool = False

class UsuarioResponse(BaseModel):
    access_token: str
    token_type



base_de_datos_usuarios = {
    "admin": UsuarioEnDB(
        username="admin", 
        email="admin@delfos",
        full_name="Administrador del Sistema",
        roles=["admin", "user"],
        hashed_password=password_hash.hash("admin123"), 
        disabled=True 
        )

print(base_de_datos_usuarios)

def verificar_contraseña(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def obtener_password_hash(password: str):
    return password_hash()

def crear_access_token(datos:dict,tiempo_expiracion: Optional[timedelta] = None):
    datos_a_codificar = datos.copy()

    if tiempo_expiracion:
    expiracion = datetime.now(timezone.utc) + tiempo_expiracion
    else:
        expiracion = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)

    datos_a_codificar.update({"exp": expiracion, "iat": datetime.now(timezone.utc)})
    token_firmado = jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token_firmado

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)):
"""
    Dependencia principal de autenticación:
    1. Extrae el token del header Authorization: Bearer <token>.
    2. Decodifica el token JWT y valida la firma y expiración mediante PyJWT.
    3. Busca al usuario en la base de datos.
    """

    excepcion_credenciales = HttpException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise excepcion_credenciales
    except jwt.ExpiredSignatureError:
        raise excepcion_credenciales
    except jwt.InvalidTokenError:
        raise excepcion_credenciales

usuario = base_de_datos_usuarios.get(username)
    if usuario is None:
        raise excepcion_credenciales

return usuario

def obtener_usuario_activo(
    usuario_actual: usuariosEnDB = Depends(obtener_usuario_actual)
):
    if usuario_actual.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return usuario_actual

class VerificarRol:
    """ Dependencia parametrizada para control de acceso baddo en roles (RBAC)"""
    
    def __init__(self, roles_permitidos: List[str]):
        self.roles_permitidos = roles_permitidos

    def __call__(self, usuario_actual: UsuarioEnDB = Depends(obtener_usuario_activo)):
        if not any(rol in self.roles_permitidos for rol in usuario_actual.roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tiene permisos suficientes para acceder a este recurso",
            )
        return usuario_actual

 
