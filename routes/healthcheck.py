from fastapi import APIRouter, status, HTTPException

healthcheck_router = APIRouter(prefix='/healthcheck', tags=['Healthcheck'])


@healthcheck_router.get('')
def healthcheck():
    try:
        return {
            'status': status.HTTP_200_OK,
            'condition': 'Healthy'
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Unexpected Error: {e}',
        )
