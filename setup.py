from setuptools import setup, find_packages

requires = [
    'python-telegram-bot',
    'vsx2_change_layout @ git+https://github.com/mcwladkoe/vsx2_change_layout',
]

setup(
    name='vsx2_change_layout_bot',
    version='1.0.0',
    description='Change Layout telegram bot',
    author='Vladyslav Samotoy',
    author_email='svevladislav@gmail.com',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requires,
    entry_points="""\
        [console_scripts]
        vsx2_change_layout_bot_run = vsx2_change_layout_bot.bot:main
    """
)
