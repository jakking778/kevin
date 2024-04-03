# kevin

## Problem Statement

It is hard to organize family and friends for events and more casual things like video games. There are some applications that allow this right now, but they are not centralized onto one service (like google). I am hoping we can keep this application as light as possible, and allow guests to freely use without a login/account. Hopefully with minimum overhead to join the server, people will be more likely to use it.

## High Level Features

### Event Planning For Future Events

Plan calender events, invite friends, RSVP

### Time Sensitive Events

Coordinate time sensitive events like "Play Helldivers 2 right now". Right now I accomplish this by separately texting each individual person and then we can plan on playing if four people have responded yes.

### Shared Lists

Grocery Lists, todo lists, or possibly even tasks tied to an event.

## Non Function Requirements

* Only admin account required
  * Guests should be free to join the server atached to a given name
* Self Hosted
  * I am fairly certain with the guest model it cannot be deployed to a central services
* Open source

## Why Is It Name Kevin?

Kevin


## Developer Setup

### Docker

To run the program in docker just build the image locally and expose port 5000

```
docker build .
docker run -p 5000:5000 $image_id_from_previous_step
```