def log_event(event):
    """Log events for monitoring and debugging."""
    with open('event_log.txt', 'a') as log_file:
        log_file.write(f"{event}\n")

---