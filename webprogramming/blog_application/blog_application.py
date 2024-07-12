from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory storage for posts
posts = []


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id]
    return render_template('post.html', post=post)


@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            posts.append({'title': title, 'content': content})
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Title and Content are required!', 'danger')
    return render_template('new_post.html')


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = posts[post_id]
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        flash('Post updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    posts.pop(post_id)
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
