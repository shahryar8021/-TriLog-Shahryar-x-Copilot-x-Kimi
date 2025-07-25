import os
from pathlib import Path

def summarize_log(log_path: Path) -> str:
    \"\"\"
    Kimi K2 placeholder. Set AI_PROVIDER=kimi to trigger live API.
    \"\"\"
    if os.getenv("AI_PROVIDER") == "kimi":
        return "Real Kimi K2 summary will be streamed here."
    return "Summary not available – agent not trained yet."
