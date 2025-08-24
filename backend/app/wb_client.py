import os
import httpx
from datetime import date, timedelta
from typing import List, Dict, Any

from .config import settings


class WBClient:
    """Клиент для работы с API Wildberries."""

    BASE_URL = "https://advert-api.wb.ru"

    def __init__(self, token: str | None = None):
        self.token = token or settings.wb_api_token or os.getenv("WB_API_TOKEN")
        self.headers = {"Authorization": self.token} if self.token else {}

    async def fetch_ads_stats(self, campaign_id: int, date_from: str, date_to: str) -> List[Dict[str, Any]]:
        """Запрос статистики по кампании (реальный вызов)."""
        if not self.token:
            raise ValueError("WB_API_TOKEN не задан")

        url = f"{self.BASE_URL}/adv/v2/fullstats"
        params = {"id": campaign_id, "dateFrom": date_from, "dateTo": date_to}

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(url, headers=self.headers, params=params)
            resp.raise_for_status()
            return resp.json()

    def fetch_ads_stats_demo(self) -> List[Dict]:
        """Генерация демо-данных (если нет токена)."""
        base = date.today()
        data: List[Dict] = []
        for i in range(7):
            d = base - timedelta(days=i)
            data.append({
                "campaign_id": "demo-1",
                "date": d.isoformat(),
                "impressions": 1000 + i * 37,
                "clicks": 100 + i * 5,
                "spend": round(50.0 + i * 2.3, 2),
                "orders": 10 + i,
                "revenue": round(200.0 + i * 11.7, 2),
            })
        return list(reversed(data))
