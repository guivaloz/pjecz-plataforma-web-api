"""
Abogados v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.abogados.crud import get_abogados, get_abogado
from plataforma_web.v2.abogados.schemas import AbogadoOut

abogados = APIRouter()


@abogados.get("", response_model=LimitOffsetPage[AbogadoOut])
async def listado_abogados(
    nombre: str = None,
    ano_desde: int = None,
    ano_hasta: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Abogados"""
    try:
        listado = get_abogados(db, nombre, ano_desde, ano_hasta)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@abogados.get("/{abogado_id}", response_model=AbogadoOut)
async def detalle_abogado(
    abogado_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Abogado a partir de su id"""
    try:
        abogado = get_abogado(db, abogado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AbogadoOut.from_orm(abogado)
