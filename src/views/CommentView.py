from flask import request, g, Blueprint, json, Response
from ..models.CommentModel import CommentModel, CommentSchema
comment_api = Blueprint('comment_api', __name__)
comment_schema = CommentSchema()

comment_api = Blueprint('comment_api', __name__)
comment_schema = CommentSchema()

def  response(res, status_code):
  """
  Custom Response
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )


@comment_api.route('/', methods=['POST'])
def create():
    """
    Creating Comment
    """
    req_data = request.get_json()

    data, error = comment_schema.load(req_data)
    if error:
        return response(error, 400)
    comment = CommentModel(data)
    comment.save()
    data = comment_schema.dump(comment).data
    return response(data, 201)


@comment_api.route('/', methods=['GET'])
def index():
    """
    Get all Comments
    """
    comments = CommentModel.get_all_comments()
    data = comment_schema.dump(comments, many=True).data
    return response(data, 201)

@comment_api.route('/<int:id>', methods=['GET'])
def show(id):
    """
    Get 1 Comment
    """
    comment = CommentModel.get_one_comment(id)
    if not comment:
        return response({'error': 'comment not found'}, 404)
    data = comment_schema.dump(comment).data
    return response(data, 200)

@comment_api.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Updating 1 Comment
    """
    req_data = request.get_json()
    comment = CommentModel.get_one_comment(id)
    if not comment:
        return response({'error': 'comment not found'}, 404)
    data = comment_schema.dump(comment).data
    data, error = comment_schema.load(req_data, partial=True)

    if error:
        return response(error, 404)

    comment.update(data)
    data = comment_schema.dump(comment).data
    return response(data, 200)

@comment_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Delete 1 Comment
    """
    comment = CommentModel.get_one_comment(id)
    if not comment:
        return response({'error': 'comment not found'}, 404)
    data = comment_schema(comment).data
    comment.delete()
    return response({'message': 'comment deleted'}, 204)
