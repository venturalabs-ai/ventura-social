from datetime import datetime, timezone
import unittest

from ventura_social import make_job, plan_batches


class SocialQueueTests(unittest.TestCase):
    def test_normalizes_job_and_utc_time(self):
        job = make_job("X", "  Hello   world  ", datetime(2026, 8, 8, 12, tzinfo=timezone.utc))
        self.assertEqual(job.platform, "twitter")
        self.assertEqual(job.content, "Hello world")
        self.assertEqual(job.scheduled_at.tzinfo, timezone.utc)

    def test_batches_are_sorted_and_bounded(self):
        jobs = [
            make_job("linkedin", f"post {i}", datetime(2026, 8, 8, 12 + (i % 2), tzinfo=timezone.utc))
            for i in range(5)
        ]
        batches = plan_batches(jobs, max_per_batch=2)
        self.assertEqual([len(batch) for batch in batches], [2, 2, 1])
        flattened = [job.scheduled_at for batch in batches for job in batch]
        self.assertEqual(flattened, sorted(flattened))

    def test_unsupported_platform_and_naive_time_fail(self):
        with self.assertRaises(ValueError):
            make_job("unknown", "hello", datetime.now(timezone.utc))
        with self.assertRaises(ValueError):
            make_job("linkedin", "hello", datetime(2026, 8, 8, 12))


if __name__ == "__main__":
    unittest.main()
