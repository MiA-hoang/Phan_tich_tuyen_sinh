def register_routes(app):
    from routes.university import university_bp
    from routes.major import major_bp
    from routes.exam_group import exam_group_bp
    from routes.admission_data import admission_data_bp

    app.register_blueprint(university_bp, url_prefix="/api/universities")
    app.register_blueprint(major_bp, url_prefix="/api/majors")
    app.register_blueprint(exam_group_bp, url_prefix="/api/exam-groups")
    app.register_blueprint(admission_data_bp, url_prefix="/api/admission-scores")