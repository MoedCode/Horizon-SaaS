# Horizon‑SaaS

[![License: AGPL‑3.0](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/yourusername/Horizon-SaaS/ci.yml?branch=main)](https://github.com/yourusername/Horizon-SaaS/actions)

> Enterprise‑grade subscription management & analytics platform, open‑source with commercial licensing.

## 🚀 Key Features

- **Automated Billing & Invoicing**: Flexible metered or recurring plans.
- **Real‑Time Analytics**: Dashboard tracking MRR, churn, LTV, and usage metrics.
- **White‑Label UI**: Customize branding, colors, and domain.
- **Seamless Payments**: Stripe integration with webhooks and dunning flow.
- **Multi‑Tenant Architecture**: Secure isolation of customer data.
- **CI/CD‑Ready**: Docker, GitHub Actions workflows for build, test, and deploy.

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (Neon)
- **Frontend**: Tailwind CSS, Alpine.js
- **Payments**: Stripe API
- **CI/CD**: GitHub Actions
- **Containerization**: Docker & Docker Compose

## 🏁 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional but recommended)
- Stripe account and API keys
- PostgreSQL instance or NeonDB

### Installation (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/Horizon-SaaS.git
   cd Horizon-SaaS
   ```
2. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Configure environment**
   - Copy `.env.example` → `.env`
   - Set `DB_URL`, `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, etc.

4. **Run migrations & start server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Using Docker

```bash
docker-compose up --build
```
Your API will be available at `http://localhost:8000`.

## 🔧 Configuration

All sensitive settings are in environment variables:

| Key                       | Description                       |
| ------------------------- | --------------------------------- |
| `DB_URL`                  | PostgreSQL connection string      |
| `STRIPE_SECRET_KEY`       | Stripe secret API key             |
| `STRIPE_PUBLISHABLE_KEY`  | Stripe publishable key            |
| `DJANGO_SECRET_KEY`       | Django secret key                 |

## ✅ Running Tests

```bash
pytest
```

## 🚢 Deployment

- Ensure your host has Docker or Python 3.10+ environment.
- Use GitHub Actions (workflow at `.github/workflows/ci.yml`) for CI, and `.github/workflows/deploy.yml` for automated deploys.
- Configure your production `.env` with live Stripe keys and DB credentials.

## 🤝 Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request.

Please follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

## 📜 License

This project is licensed under the [GNU AGPL v3.0](LICENSE). Commercial licensing is available—please contact sales@horizon-saas.com for details.

---

*Feel free to add more sections (e.g., troubleshooting, roadmap, architecture) as your project grows.*

