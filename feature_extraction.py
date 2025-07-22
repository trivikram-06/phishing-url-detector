from bs4 import BeautifulSoup
import re

def extract_content_features(html, url):
    soup = BeautifulSoup(html, "html.parser")
    features = {}

    # Example features:
    features["has_login_form"] = int(bool(soup.find("input", {"type": "password"})))
    features["num_input_tags"] = len(soup.find_all("input"))
    features["num_external_links"] = len([a for a in soup.find_all("a", href=True) if url.split("/")[2] not in a['href']])
    features["contains_iframe"] = int(bool(soup.find("iframe")))
    features["contains_script"] = int(bool(soup.find("script")))

    # suspicious words
    text = soup.get_text().lower()
    suspicious_words = ["verify", "account", "login", "bank", "password"]
    features["suspicious_word_count"] = sum(word in text for word in suspicious_words)

    return list(features.values())
