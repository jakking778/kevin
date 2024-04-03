FROM node:21 as frontend_build

COPY /kevins_frontend .
RUN yarn install
RUN yarn run build


FROM python:3.12 as run_time

workdir /app
RUN mkdir static
COPY --from=frontend_build /build/ static/
COPY kevins_backend .
RUN pip install poetry
RUN cd kevins_backend
RUN poetry install
RUN which python
RUN which python3

EXPOSE 5000
CMD poetry run python -m kevins_backend