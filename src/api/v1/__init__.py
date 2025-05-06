import fastapi

from .probe import router as probe_router
from .mfcr import router as mfcr_router


router = fastapi.APIRouter(
    prefix="/api/v1",
)

router.include_router(probe_router)
router.include_router(mfcr_router)
