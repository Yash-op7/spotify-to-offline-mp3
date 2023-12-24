import csv

def save_json_list_to_csv(json_list, csv_file_path):
    if len(json_list) > 0:
        # Extract the keys from the first record to use as column headers
        headers = list(json_list[0].keys())

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=headers)

            # Write headers to the CSV file
            csv_writer.writeheader()

            # Write data to the CSV file
            csv_writer.writerows(json_list)

        print(f"Data successfully saved to {csv_file_path}")
    else:
        print("No data to save.")


def get_artist_and_song_names(songs):
    song_names = [song['track']['name'] for song in songs]
    artist_names = [" ".join([artist['name'] for artist in song['track']['album']['artists']]) for song in songs]
    data = [{'song':song, 'artist':artist} for song, artist in zip(song_names, artist_names)]
    return data


