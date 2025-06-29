from processor_regex import classify_with_regex

def classify(logs):
    labels = [ ]
    for source, log_msg in  logs:
       label = classify_log(source,log_msg)
       labels.append(label)
    return labels

def classify_log(source, log_message):

    if source == "LegacyCRM":
        pass # LLM
    else:
        label = classify_with_regex(log_message)
        if label is None:
            pass # BERT
        return label

if "__name__" == "__main__":
    logs = [
        ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
        ("BillingSystem", "User 12345 Logged in."),
        ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
    ]

