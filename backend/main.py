from app import create_app
import flask

app = create_app()

def print_routes(app):
    print(f"{'Endpoint':<40} {'Methods':<20} {'Rule'}")
    for rule in app.url_map.iter_rules():
        methods = ', '.join(rule.methods - {'OPTIONS', 'HEAD'})
        print(f"{rule.endpoint:<40} {methods:<20} {rule.rule}")


if __name__ == "__main__":
    app.run(debug=True)
    print_routes(app)