FROM python:3.14.5-alpine3.23

# App information
ENV app_name=django-muflopping
ENV app_version=0.1.0

# Container metadata
LABEL maintainer="ilmuflone"
LABEL maintainer_email="muflone@muflone.com"
LABEL app_name="Django Muflopping"
LABEL app_version="${app_version}"

# Install and execute application
ADD "https://github.com/muflone/django-muflopping/archive/${app_version}.tar.gz" "/tmp/${app_name}-${app_version}.tar.gz"
RUN tar xzf "/tmp/${app_name}-${app_version}.tar.gz" -C "/tmp" && \
    rm "/tmp/${app_name}-${app_version}.tar.gz" && \
    mv "/tmp/${app_name}-${app_version}" "/app" && \
    echo "SECRET_KEY = '$(date +%s | sha256sum | base64 | head -c 50)'" >> "/app/project/settings_container.py" && \
    echo "ALLOWED_HOSTS = '*'" >> "/app/project/settings_container.py" && \
    mkdir "/app/static" && \
    pip install -r /app/requirements.txt && \
    touch /var/lib/django-muflopping.sqlite3
EXPOSE 8080/tcp
CMD ["bash", "/app/container-launch.sh", "8080"]

