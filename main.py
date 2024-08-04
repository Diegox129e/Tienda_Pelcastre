
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from api.api_V1.router import router
from core.config import settings
from docs import tags_metadata
from models.debtors import Debtors
from models.doubt_to_supplier import DoubtToSupplier
from models.losses import Losses
from models.product import Products
from models.receive_supplier import ReceiveSupplier
from models.replacement_of_goods import ReplacementOfGoods
from models.sale_of_a_product import SaleOfAProduct
from models.sale_of_two_or_more_products import SaleOfTwoOrMoreProducts

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Esta es una aplicacion de ventas para la tienda Pelcastre",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata,
    debug=True,
)


@app.on_event("startup")
async def app_init():
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).tiendaPelcastre

    await init_beanie(
        database=db_client,
        document_models=[
            Products,
            Debtors,
            DoubtToSupplier,
            Losses,
            ReceiveSupplier,
            ReplacementOfGoods,
            SaleOfAProduct,
            SaleOfTwoOrMoreProducts,
        ]
    )

app.include_router(router, prefix=settings.API_V1_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
