# Vision Playground

Explore grayscale convolution, blur, and Sobel edges using a generated image and numeric output.

An AI-assisted educational portfolio project prepared for Erik Vera's internship learning. This is a working prototype, not production software. Authorship and skills should be represented based on what you can explain and change independently.

## Try in your browser

[Open the live demo](https://erickvera610.github.io/vision-playground/). The static JavaScript demo runs on the visitor's device and cannot change repository code. The Python implementation below provides the local backend. ML random-number generators differ between runtimes, so exact metrics differ. Tracker browser storage is localStorage; Python storage is SQLite.

## Run in two minutes

Requires Python 3.11 or newer; no pip dependencies.

```bash
git clone https://github.com/erickvera610/vision-playground.git
cd vision-playground
python app.py
```

Open http://127.0.0.1:8000. On Windows, use `py app.py` if `python` is unavailable. Stop with Ctrl+C. Run `python -m unittest discover -v` to execute tests.

## Architecture

- `index.html`: responsive accessible interface; renders output with textContent.
- `app.py`: local HTTP service, `/health`, and validated JSON POST `/api/run`.
- `core.py`: domain logic separated from transport and presentation.
- `test_core.py`: deterministic behavior and failure cases.
- `.github/workflows/tests.yml`: Python 3.11 and 3.12 CI.
- `TUTORIAL_ES.md`: beginner Spanish guide and interview practice.

## API

POST a JSON object to `/api/run`; inputs are the same fields used by the interface. Responses are JSON. Invalid inputs return 400; unknown paths return 404. GET `/health` returns `{"status":"ok"}`.

## Design and limits

Una imagen es una matriz de intensidades entre 0 y 255. Convolución combina cada píxel con sus ocho vecinos usando una matriz 3 por 3. El desenfoque calcula promedios. Sobel calcula cambios horizontales y verticales; su magnitud resalta bordes. En la frontera repito el píxel más cercano. Este laboratorio usa una figura generada, no un modelo de reconocimiento de objetos.

The built-in HTTP server is for a local demonstration. There is no authentication, rate limiting, or public production deployment. Never enter personal application records on a publicly exposed demo. Bind to localhost by default. For Codespaces only, run `HOST=0.0.0.0 python app.py` and keep the forwarded port private; usage may consume your GitHub quota.

## Review and contribution workflow

Create a feature branch, make one small change, run the tests, commit it, push the branch, and open a pull request. Explain the change and validation. Do not fabricate collaboration or commit history. Suggested first improvement: add a new input option with one behavior test and update this README.

## References

- https://docs.python.org/3/library/http.server.html
- https://docs.github.com/en/actions/tutorials/build-and-test-code/python

License: MIT.
