FROM apify/actor-python:3.13

USER root

RUN echo "Installing Playwright Chromium..." \
    && playwright install --with-deps chromium \
    && echo "Chromium installation complete."

USER myuser

COPY --chown=myuser:myuser requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=myuser:myuser . ./

RUN python3 -m compileall -q src/

CMD ["python3", "-m", "src"]
