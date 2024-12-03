import os

import click
import requests


@click.command()
@click.option("-k", "--api-key", required=True, help="API key for Tenor")
@click.option(
    "-q",
    "--search",
    "search_term",
    default="technology",
    show_default=True,
    help="Search term for GIFs",
)
def random_gif(api_key, search_term, limit=1):
    """
    Downloads a random GIF matching the given search term from Tenor and saves it to
    a file named after the search term in the "outputs" directory.
    """
    random_gif_url = f"https://g.tenor.com/v1/random?q={search_term}&key={api_key}&limit={limit}&ar_range=standard&media_filter=minimal"
    response = requests.get(random_gif_url, timeout=10)
    response.raise_for_status()
    result = response.json()
    result = result["results"][0]
    gif_url = result["media"][0]["gif"]["url"]
    output_path = f"outputs/{search_term}.gif"

    if not os.path.exists("outputs"):
        os.mkdir("outputs")

    with open(output_path, "wb") as f:
        f.write(requests.get(gif_url, timeout=10).content)

    # display gif_url
    click.echo(f"👍 GIF URL: {gif_url}")
    click.echo(f"🎉 New GIF saved to {output_path}")


def main():
    random_gif()


if __name__ == "__main__":
    main()
