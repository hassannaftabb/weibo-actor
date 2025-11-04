FROM apify/actor-python:3.13

USER myuser

COPY --chown=myuser:myuser requirements.txt ./

RUN echo "Installing dependencies..." \
    && python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && echo "Python packages installed:" \
    && pip freeze

RUN echo "Installing Playwright Chromium..." \
    && playwright install --with-deps chromium \
    && echo "Chromium installation complete."

COPY --chown=myuser:myuser . .

RUN python3 -m compileall -q src/

ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

CMD ["python3", "-m", "src"]
