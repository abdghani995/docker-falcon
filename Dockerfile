ARG PYTHON_VERSION=3.6
FROM python:${PYTHON_VERSION} as builder
MAINTAINER Alexandre Ferland <aferlandqc@gmail.com>

WORKDIR /build
COPY requirements.txt /build/
RUN pip wheel -r requirements.txt

FROM python:${PYTHON_VERSION}

COPY --from=builder /build /build

RUN pip install -r /build/requirements.txt \
                -f /build \
                && rm -rf /build \
                && rm -rf /root/.cache/pip
WORKDIR /app
COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python", "run.py"]
