#SPERIMENTAL WIP

source ../.env

#term="ritorno al futuro parte"

term=$1

#URL Encoding Term
term_encoded=$(printf %s "${term}" | jq -sRr @uri)

response="$(curl \
  --location 'http://localhost:7878/api/v3/movie/lookup?term='"${term_encoded}" \
  --header 'X-Api-Key: '"${RADARR_API_KEY}")"

total_result="$(echo "${response}" | jq '.')"

for i in $total_result
do
   echo "$i"
done

title="$(echo "${response}" | jq -r '.[0].title')"
year="($(echo "${response}" | jq -r '.[0].year'))"

echo "${title} ${year}"