#Get project env
source ../.env

#Get movie data from input
echo "Enter the Movie Title:"
read -r MOVIE_TITLE

echo "Enter the Movie Release Year:"
read -r MOVIE_YEAR

echo "Enter MEGA Movie Link:"
read -r MOVIE_URL

#Create movie directory and go inside it
MOVIE_DIR="${MOVIES_PATH}/${MOVIE_TITLE} (${MOVIE_YEAR})"
mkdir "${MOVIE_DIR}"
cd "${MOVIE_DIR}" || exit

#Download media
megadl "${MOVIE_URL}"

echo "Enjoy 😜"