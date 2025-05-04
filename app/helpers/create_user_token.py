from flask_jwt_extended import create_access_token

def create_user_token(user):
    additional_claims = {
        "email": user.email,
        "perms_1_allowed": str(user.perms_1_allowed),
        "perms_2_allowed": str(user.perms_2_allowed),
        "perms_3_allowed": str(user.perms_3_allowed)
    }
    
    access_token = create_access_token(
        identity=str(user.id),
        additional_claims=additional_claims
    )
    return access_token