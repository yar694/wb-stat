import os
from datetime import date, timedelta
from typing import List, Dict

from .config import settings

class WBClient:
    """Клиент Wildberries API (пока демо).

    В будущем сюда добавим реальные запросы к WB ADS/STAT API через httpx.
    Токен берём из переменных окружения (.env).
    """
    def __init__(self, token: str | None = None):
        self.token = token or settings.wb_api_token or os.getenv("WB_API_TOKEN")

    def fetch_ads_stats_demo(self) -> List[Dict]:
        """Генерируем демо-статистику за последние 7 дней."""
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