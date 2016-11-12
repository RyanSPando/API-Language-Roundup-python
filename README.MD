#API Language Round Up - Python/Flask
### The API language round up attempts to make a simple crud route for a donut.  The API should return the properly formatted JSON for the route in question.  Post and Delete routes should return the new entry.  Delete route should return the deleted entry.
Live API Entry point
https://dashboard.heroku.com/apps/api-language-roundup-python/donuts
## Donut DB schema

|donut
|----------------
|id
|name (text)
|topping (text)
|price (int)

## Donut Routes and Pages

| Route Name      | Method   | Example URL        | Route                |
|-----------------|----------|--------------------|----------------------|
| donuts index    | `GET`    | `/donuts`          | `/donuts`            |
| donut get       | `GET`    | `/donuts/1/`       | `/donuts/:id`        |
| donut edit      | `PUT`    | `/donuts/1/edit`   | `/donuts/:id/edit`   |
| donut create    | `POST`   | `/donuts`          | `/donuts`            |
| donut destroy   | `DELETE` | `/donuts/1/delete` | `/donuts/:id/delete` |
