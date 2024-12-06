import os

import click
import requests

from src.giphy import GiphyApi
from src.tenor import TenorApi


@click.command()
@click.option("-k", "--api-key", required=True, help="API key for Tenor and Giphy")
@click.option(
    "-q",
    "--search",
    "search_term",
    default="meme",
    show_default=True,
    help="Search term for GIF",
)
@click.option(
    "-s",
    "--source",
    default="GIPHY",
    type=click.Choice(["Tenor", "GIPHY"], case_sensitive=False),
    show_default=True,
    help="Source for GIF",
)
def random_gif(api_key, search_term, source):
    """
    Downloads a random GIF matching the given search term from the given source and
    saves it to a file named after the search term in the "outputs" directory.
    """
    match source.lower():
        case "tenor":
            source_api = TenorApi(api_key)
        case "giphy":
            source_api = GiphyApi(api_key)

    gif_url, detail = source_api.random_gif(search_term)
    output_path = f"outputs/{search_term}.gif".replace(" ", "_")
    if not os.path.exists("outputs"):
        os.mkdir("outputs")

    with open(output_path, "wb") as f:
        f.write(requests.get(gif_url, timeout=10).content)

    # display gif_url
    click.echo(f"😎 GIF URL: {gif_url}")
    click.echo(f"🍹 Detail: {detail}")
    click.echo(f"🎁 New GIF saved to {output_path}")


def main():
    random_gif()


if __name__ == "__main__":
    main()
