#!/usr/bin/env python3
"""Observer pattern: a news subject with topic-filtered observers."""


class NewsSubject:
    """Publish news events to subscribed observers."""

    def __init__(self) -> None:
        """Start with no observers."""
        self._observers = []

    def subscribe(self, observer, topics=None) -> None:
        """Subscribe an observer, optionally to specific topics only."""
        wanted = None if topics is None else set(topics)
        self._observers.append((observer, wanted))

    def unsubscribe(self, observer) -> None:
        """Remove an observer."""
        self._observers = [
            (obs, topics) for obs, topics in self._observers
            if obs is not observer
        ]

    def notify(self, topic: str, data: str) -> None:
        """Send an event to every observer interested in the topic."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Log every event it receives."""

    def update(self, topic: str, data: str) -> None:
        """Print the event as a log line."""
        print("log:{}={}".format(topic, data))


class EmailObserver:
    """Email every event it receives."""

    def update(self, topic: str, data: str) -> None:
        """Print the event as an email line."""
        print("email:{}={}".format(topic, data))


class SmsObserver:
    """Send an SMS for every event it receives."""

    def update(self, topic: str, data: str) -> None:
        """Print the event as an SMS line."""
        print("sms:{}={}".format(topic, data))


def main() -> None:
    """Wire the observers to a subject and publish three events."""
    subject = NewsSubject()
    subject.subscribe(LogObserver(), topics={"sports", "breaking"})
    subject.subscribe(EmailObserver())
    subject.subscribe(SmsObserver(), topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
