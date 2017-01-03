"""Main flask app."""
import sys
import logging

from flask import (Flask, Response, request, session, g, redirect,
                   url_for, abort, render_template)
from flask_frozen import Freezer
import config


logging.basicConfig()
log = logging.getLogger('main')


app = Flask(import_name=__name__,
            static_folder='static',
            template_folder='templates')

app.config.from_object(config)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
freezer = Freezer(app)


if app.config.get('DEBUG'):
    log.setLevel(logging.DEBUG)

    class XhtmlResponse(Response):
        """A class that defaults to using XHTML instead of HTML.

        If no mimetype is specified. Useful for checking for wellformed HTML.
        """

        default_mimetype = 'application/xhtml+xml'

    app.response_class = XhtmlResponse


_features = [{'fa_icon': 'fa-sliders',
              'title': 'Dashboard',
              'blurb': 'Single pane of glass management of workstations, servers, '
                       'storage, software tools, User/Group membership and access privileges.',
              'btn_link': ''
             },
             {'fa_icon': 'fa-linux',
              'title': 'Linux Support',
              'blurb': 'The first choice, industrial strength OS for VFX and Animation. '
                       'Let us handle the details for you.',
              'btn_link': ''
             },
             {'fa_icon': 'fa-windows',
              'title': 'Windows Support',
              'blurb': 'We acknowledge some software only runs on Windows. '
                       'Don\'t sweat it, we support that too.',
              'btn_link': ''
             },
             {'fa_icon': 'fa-cog',
              'title': 'Render Farm',
              'blurb': 'Built-in render farm with pay-as-you-go compute and software '
                       'licensing. Don\'t pay for render power until you actually need it!',
              'btn_link': ''
             },
             {'fa_icon': 'fa-bar-chart',
              'title': 'Clear Pricing',
              'blurb': 'Pay-as-you-go pricing makes it easy to estimate and budget '
                       'using the built-in cost estimator.',
              'btn_link': ''
             },
             {'fa_icon': 'fa-lock',
              'title': 'Secure By Default',
              'blurb': 'Desktop is streamed to users and all production data stays '
                       'securely in the cloud. Stateless clients are bomb-proof; '
                       'they return to a clean state after each reboot.',
              'btn_link': ''
             },
            ]


@app.route('/')
def root():
    """Website root."""
    data = {'features': _features}
    content = render_template('index.xhtml', data=data)
    return content


@app.route('/contact/')
def contact():
    """Route for contact page."""
    content = render_template('contact.xhtml')
    return content


@app.route('/team/')
def team():
    """Route for team page."""
    data = {'team_members': _get_team_members()}
    data['team_members'].extend(_get_advisors())
    content = render_template('team.xhtml', data=data)
    return content


@app.route('/404.html')
def four_oh_four():
    """Route for 404 page."""
    return render_template('404.xhtml')


@app.errorhandler(404)
def page_not_found(error):
    """Error page for 404."""
    return redirect(url_for('four_oh_four'))


def _get_advisors():
    """Because url_for only works when the app context exists, put this in a function."""
    _advisors = [{'img_src': url_for('static', filename='jared-sq.jpg'),
                  'name': 'Jared Tarbell',
                  'title': 'Advisor',
                  'blurb': 'Jared holds a BS in Computer Science from New Mexico '
                           'State University. Co-founder of Etsy. Creator of beautiful '
                           'computational artifacts. All around great guy.',
                  'facebook': '#',
                  'linkedin': '#',
                  'twitter': '#'
                 },
                 {'img_src': url_for('static', filename='greg-sq.jpg'),
                  'name': 'Greg Ercolano',
                  'title': 'Technical Advisor',
                  'blurb': 'A technical wizard, Greg has won a Technical Academy Award '
                           'for the render farm queue "Rush", which is used at companies '
                           'such as Blue Sky Studios and Zoic Studios. Owner of Seriss '
                           'Corporation.',
                  'facebook': '#',
                  'linkedin': '#',
                  'twitter': '#'
                 },
                ]
    return _advisors


def _get_team_members():
    """Because url_for only works when the app context exists, put this in a function."""
    # TODO: find out how to move this into something like json or other data storage
    _team_members = [{'img_src': url_for('static', filename='aaron-sq.jpg'),
                      'name': 'Aaron Estrada',
                      'title': 'Founder & CEO',
                      'blurb': '20 year Veteran of VFX and animation. Former CTO and VFX '
                               'Supervisor for boutique feature VFX studio Pivot VFX. '
                               'To date, has built three VFX/animation pipelines and used '
                               'countless others on feature and TV production. Previous '
                               'employers include Dreamworks Animation, Sony Pictures Imageworks, '
                               'Rhythm and Hues, Nickelodeon and Sony Development. '
                               'Having worked the first ten years of his career as a generalist, '
                               'Aaron is well versed in all stages of C.G. production.',
                      'facebook': '#',
                      'linkedin': '#',
                      'twitter': '#'
                     },
                     {'img_src': url_for('static', filename='ethan-sq.jpg'),
                      'name': 'Ethan Estrada',
                      'title': 'Founder & CTO',
                      'blurb': 'Studied Animation and Computer Science in Brigham Young '
                               'University\'s multi-award winning Center for Animation. '
                               'Cut his teeth supporting Linux at Novell, where he learned '
                               'first hand the importance of staying connected with clients. '
                               'A Houdini and Linux expert, Ethan works as Pipeline TD '
                               '(and occasional FX TD) at a small VFX shop in the Salt Lake City, '
                               'Utah area. When he has the time, he enjoys practicing '
                               'Brazilian Jiu-Jitsu.',
                      'facebook': '#',
                      'linkedin': '#',
                      'twitter': '#'
                     },
                     {'img_src': url_for('static', filename='aj-sq.jpg'),
                      'name': 'AJ Creek',
                      'title': 'VP of Operations',
                      'blurb': 'Graduated with a BFA in Animation from Brigham Young University. '
                               'A proficient 3D generalist, he\'s worked at Stereo D and '
                               'contributed to independent projects. AJ is a natural at '
                               'getting people excited about a cause. While at BYU-Idaho, he '
                               'single-handedly organized, promoted, and ran a 32-team, '
                               'double elimination indoor soccer tournament (without having a '
                               'single fight or red card) which led to the creation of '
                               'the intramural indoor soccer program there.',
                      'facebook': '#',
                      'linkedin': '#',
                      'twitter': '#'
                     },
                     {'img_src': url_for('static', filename='liz-sq.jpg'),
                      'name': 'Elizabeth Brayton',
                      'title': 'Software Engineer',
                      'blurb': 'Holds a BS in Computer Science with an emphasis in Animation '
                               'from Brigham Young University. After graduation she has '
                               'worked as a VFX artist and Pipeline Technical Director. Her '
                               'special skills involve being a super VFX ninja!',
                      'facebook': '#',
                      'linkedin': '#',
                      'twitter': '#'
                     }
                    ]
    return _team_members

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='localhost', port=8080)
