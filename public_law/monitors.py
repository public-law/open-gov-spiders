from spidermon import Monitor, MonitorSuite, monitors


@monitors.name("Item count")
class ItemCountMonitor(Monitor):
    @monitors.name("Minimum number of items")
    def test_minimum_number_of_items(self):
        item_extracted = getattr(self.data.stats, "item_scraped_count", 0)
        minimum_threshold = 9

        self.assertTrue(
            item_extracted >= minimum_threshold,
            msg=f"Extracted less than {minimum_threshold} items",
        )


class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        ItemCountMonitor,
    ]