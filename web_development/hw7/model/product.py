from enum import Enum
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Sequence, DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

from .base_model import BaseModel


class ProductRecordType(Enum):
    auto: 'auto'
    manual: 'manual'


class Product(BaseModel):
    __tablename__ = 'site_acct_data'
    record_id: Mapped[int] = mapped_column(BigInteger, Sequence('product_price_rec_seq', start=1, increment=1),
                                           name='record_id', primary_key=True),
    record_type: Mapped[ProductRecordType] = mapped_column(SQLEnum(ProductRecordType), name='record_type', nullable=False),
    create_at: Mapped[datetime] = mapped_column(DateTime, name='created_at', nullable=False),
    product_id: Mapped[int] = mapped_column(BigInteger, name='product_id', nullable=False),
    product_name: Mapped[str] = mapped_column(String, name='product_name', nullable=False),
    product_status: Mapped[Optional[str]] = mapped_column(String, name='product_status', nullable=True),
    product_price_old: Mapped[Optional[int]] = mapped_column(Integer, name='product_price_old', nullable=True),
    product_price_old_curr: Mapped[Optional[str]] = mapped_column(String, name='product_price_old_curr', nullable=True),
    product_price_new: Mapped[Optional[int]] = mapped_column(Integer, name='product_price_old', nullable=True),
    product_price_new_curr: Mapped[Optional[str]] = mapped_column(String, name='product_price_new_curr', nullable=True),
