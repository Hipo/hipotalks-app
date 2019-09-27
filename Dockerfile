FROM python:3.7.0 as base

# Development
RUN apt-get update && apt-get install -y --no-install-recommends gettext \
  graphviz \
  libgdal-dev \
  postgresql-client

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
  libcairo2 \
  libffi-dev \
  libgdk-pixbuf2.0-0 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  python3-cffi \
  python3-dev \
  python3-pip \
  python3-setuptools \
  python3-wheel \
  shared-mime-info


COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

WORKDIR /hipotalks

FROM base as application_development

FROM base as application
COPY . .