from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..wb_client import WBClient

router = APIRouter()

class AdStat(BaseModel):
    campaign_id: str
    date: str
    impressions: int
    clicks: int
    spend: float
    orders: int
    revenue: float

def get_client() -> WBClient:
    return WBClient()

@router.get("/ads/stats", response_model=List[AdStat], summary="Статистика рекламной кампании (демо)")
def get_ads_stats(client: WBClient = Depends(get_client)):
    return client.fetch_ads_stats_demo()