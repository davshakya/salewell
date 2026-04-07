# Deploying SaleWell on cPanel

This repository is now prepared for a cPanel + Passenger deployment flow.

## 1. Push these files to GitHub

Your cPanel Git deployment screen requires:

- a checked-in `.cpanel.yml` file at the repo root
- a clean repository state on the branch you deploy

Commit and push your local changes before using **Update from Remote** or **Deploy HEAD Commit** in cPanel.

## 2. Create the Python app in cPanel

In **cPanel -> Application Manager** create a Python application with values like these:

- **Application root**: `salewell_app`
- **Application URL**: your main domain or the path where you want the site to live
- **Application startup file**: `passenger_wsgi.py`
- **Application Entry point**: `application`

The `.cpanel.yml` file copies this repository into `/home/salewellco/salewell_app`.
If you choose a different application root in cPanel, update the `DEPLOYPATH` line in `.cpanel.yml` to match it.

## 3. Install Python packages on the server

After creating the app, cPanel shows a command to activate the virtual environment. Run that command in cPanel Terminal, then install dependencies:

```bash
pip install -r /home/salewellco/salewell_app/requirements.txt
```

## 4. Set environment variables in Application Manager

Add these environment variables in the Python application's settings:

- `DJANGO_DEBUG=False`
- `DJANGO_SECRET_KEY=<your-new-production-secret>`
- `DJANGO_ALLOWED_HOSTS=salewell.co.in,www.salewell.co.in`
- `DJANGO_CSRF_TRUSTED_ORIGINS=https://salewell.co.in,https://www.salewell.co.in`
- `DJANGO_DB_PATH=/home/salewellco/salewell_data/db.sqlite3`
- `DJANGO_TIME_ZONE=Asia/Kolkata`

## 5. Run Django setup commands on the server

Inside the activated virtual environment, run:

```bash
python /home/salewellco/salewell_app/manage.py migrate
python /home/salewellco/salewell_app/manage.py collectstatic --noinput
```

If you want an admin login:

```bash
python /home/salewellco/salewell_app/manage.py createsuperuser
```

## 6. Deploy from Git Version Control

In **cPanel -> Git Version Control**:

1. Click **Update from Remote**
2. Click **Deploy HEAD Commit**

That deploy step copies the repository into your Python app directory through `.cpanel.yml`.

## 7. Restart the Python app

Back in **Application Manager**, restart the app after each deployment.

If static files or dependencies changed, rerun:

```bash
pip install -r /home/salewellco/salewell_app/requirements.txt
python /home/salewellco/salewell_app/manage.py collectstatic --noinput
```

## Important security note

The current `config.yml` file contains live FTP credentials. Do not keep real secrets in Git.
Rotate that FTP password, remove `config.yml` from version control, and keep only a local example file if you still need the FTP scripts.
