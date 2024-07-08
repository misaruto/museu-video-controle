from src.model.session_model import SessionResponseModel
from server.src.model.db_models.rmi_server_session_model import RmiServerSessionModel
def session_db_model_to_response_model(session:RmiServerSessionModel) -> SessionResponseModel:
  return SessionResponseModel(
    cdSessionToken=session.cd_rmi_server_session_token,
    dtfSession=session.dtf_expected_rmi_server_session,
    qtSessionDurationSeconds=session.qt_session_duration_seconds,
    nmUserName=session.nm_user_created_session
  )