FROM ruby:3.1

WORKDIR /app

COPY Gemfile /app/
RUN bundle install

COPY . /app/
CMD ["rackup", "-o", "0.0.0.0"]
