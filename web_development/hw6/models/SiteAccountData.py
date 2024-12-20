from typing import Optional

from sqlalchemy import ForeignKey, String, Integer, UniqueConstraint, Sequence
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import BaseModel
from .types import LoginType


class SiteAccountData(BaseModel):
    __tablename__ = 'site_acct_data'
    record_id: Mapped[int] = mapped_column(Integer, Sequence('site_acct_data_seq', start=1, increment=1), name='rec_id', primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), name='usr_id', nullable=False)
    site_url: Mapped[str] = mapped_column(String(100), name='site_url', nullable=False)
    login_type: Mapped[LoginType] = mapped_column(SQLEnum(LoginType), name='account_type', nullable=False)
    login_user_name: Mapped[str] = mapped_column(String(100), name='site_login', nullable=False)
    login_password: Mapped[Optional[str]] = mapped_column(String(100), name='site_password')

    __table_args__ = (
        UniqueConstraint('usr_id', 'site_url', 'account_type', name='site_acct_data_unq_idx'),
    )

    def to_dict(self) -> dict:
        return {
            'record_id': self.record_id,
            'user_id': self.user_id,
            'site_url': self.site_url,
            'login_type': self.login_type,
            'login_user_name': self.login_user_name,
            'login_password': self.login_password,
        }
