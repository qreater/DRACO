# 🐉 DRACO AI

**Developer Resourceful AI Command Operator**

```
    .___                           
  __| _/___________    ____  ____  
 / __ |\_  __ \__  \ _/ ___\/  _ \ 
/ /_/ | |  | \// __ \\  \__(  <_> )
\____ | |__|  (____  /\___  >____/ 
     \/            \/     \/      
```

DRACO is a lightweight CLI tool that translates plain-English descriptions into terminal commands using AI. Instead of searching Stack Overflow or man pages, just ask DRACO what you need.

---

## How It Works

Describe what you want to do in natural language, and DRACO queries **Llama 3.3-70B** (via Together AI) to return the exact CLI command — no extra explanation, just the command.

```bash
$ draco "find all .log files modified in the last 24 hours"
# DRACO AI Suggests:
# find . -name "*.log" -mtime -1
```

If your query isn't CLI-related, DRACO will let you know rather than hallucinate a response.

---

## Installation

### Prerequisites

- Python 3.8+
- A [Together AI](https://www.together.ai/) API key (free tier available)

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/draco.git
cd draco

# Install dependencies
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# Then edit .env and add your Together AI key:
#   API_KEY=your_together_api_key_here
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `together` | Together AI Python client |
| `rich` | Terminal formatting and colors |
| `python-dotenv` | Environment variable management |

---

## Usage

### Quick Query

Pass your question directly as an argument:

```bash
python draco.py "list all running docker containers"
python draco.py "compress a folder into a tar.gz"
python draco.py "show disk usage sorted by size"
```

### Interactive Mode

Launch an ongoing session to ask multiple questions:

```bash
python draco.py --interactive
```

### Help

```bash
python draco.py --help
```

---

## Configuration

Create a `.env` file in the project root:

```env
API_KEY=your_together_ai_api_key
```

You can get a free API key at [api.together.xyz](https://api.together.xyz/).

---

## Project Structure

```
draco/
├── draco.py          # Entry point and CLI argument parsing
├── draco/
│   ├── llm.py        # Together AI integration
│   └── options.py    # Interactive mode logic
├── .env              # API key (not committed)
├── .env.example      # Template for environment variables
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Examples

```bash
$ draco "list kubernetes pods in all namespaces"
kubectl get pods --all-namespaces

$ draco "show git branches sorted by last commit date"
git branch --sort=-committerdate

$ draco "what is the meaning of life"
❌ The given query is not CLI related.
```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Powered by [Meta Llama 3.3-70B](https://ai.meta.com/llama/) via [Together AI](https://www.together.ai/)
- Terminal styling by [Rich](https://github.com/Textualize/rich)
