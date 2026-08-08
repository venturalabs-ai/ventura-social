from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class SocialJob:
    platform: str
    content: str
    scheduled_at: datetime


def normalize_platform(platform: str) -> str:
    value = platform.strip().lower()
    aliases = {"x": "twitter", "linkedin.com": "linkedin", "instagram.com": "instagram"}
    value = aliases.get(value, value)
    allowed = {"linkedin", "instagram", "twitter"}
    if value not in allowed:
        raise ValueError(f"unsupported platform: {platform}")
    return value


def validate_content(content: str, max_chars: int = 3000) -> str:
    cleaned = " ".join(content.split())
    if not cleaned:
        raise ValueError("content is empty")
    if len(cleaned) > max_chars:
        raise ValueError("content exceeds configured limit")
    return cleaned


def make_job(platform: str, content: str, scheduled_at: datetime) -> SocialJob:
    if scheduled_at.tzinfo is None:
        raise ValueError("scheduled_at must be timezone-aware")
    return SocialJob(normalize_platform(platform), validate_content(content), scheduled_at.astimezone(timezone.utc))


def plan_batches(jobs: list[SocialJob], max_per_batch: int = 10) -> list[list[SocialJob]]:
    """Deterministic local queue planning; no external posting side effects."""
    if max_per_batch <= 0:
        raise ValueError("max_per_batch must be positive")
    ordered = sorted(jobs, key=lambda job: (job.scheduled_at, job.platform, job.content))
    return [ordered[i:i + max_per_batch] for i in range(0, len(ordered), max_per_batch)]
