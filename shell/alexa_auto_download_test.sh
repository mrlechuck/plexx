#EXPERIMENTAL WIP

source ../.env

#term="ritorno al futuro parte"

term=$*

#URL Encoding Term
term_encoded=$(printf %s "${term}" | jq -sRr @uri)

movie_data="$(curl \
  --location 'http://localhost:7878/api/v3/movie/lookup?term='"${term_encoded}" \
  --header 'X-Api-Key: '"${RADARR_API_KEY}")"

# Length
# total_result="$(echo "${response}" | jq '. | length')"

data="$(echo "${movie_data}" | jq -r '.[] += {"addOptions": {
                                                                "monitor": "movieOnly",
                                                                "searchForMovie": true
                                                              }
                                              }')"

data="$(echo "${data}" | jq -r '.[].qualityProfileId = 1')"
data="$(echo "${data}" | jq -r '.[].monitored = true')"
data="$(echo "${data}" | jq -r '.[].minimumAvailability = "announced"')"
data="$(echo "${data}" | jq -r '.[].rootFolderPath = "/movies"')"
data="$(echo "${data}" | jq -r '.[0]')"

movie_add="$(curl \
  --location 'http://localhost:7878/api/v3/movie' \
  --header 'Content-Type: application/json' \
  --data "${data}" \
  --header 'X-Api-Key: '"${RADARR_API_KEY}")"

echo "${movie_add}"