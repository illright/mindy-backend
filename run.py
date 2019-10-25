"""Run script"""

import os

from app.main import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()
else:
    app = create_app()  # pylint: disable=invalid-name
