from src.dto.session_dto import RmiServerSessionResponseDto
from src.model.rmi_server_session_model import RmiServerSessionModel
def session_db_model_to_response_model(session:RmiServerSessionModel) -> RmiServerSessionModel:
  return RmiServerSessionModel(
    cdSessionToken=session.cd_rmi_server_session_token,
    dtfSession=session.dtf_expected_rmi_server_session,
    qtSessionDurationSeconds=session.qt_session_duration_seconds,
    nmUserName=session.nm_user_created_session
  )