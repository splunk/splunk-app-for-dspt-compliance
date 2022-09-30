from apiclient import (
    APIClient,
    paginated,
    retry_request,
)

def get_next_page(response, previous_page_params):
    """
    See specification at:
    https://digital.nhs.uk/services/data-security-centre/cyber-alerts-api/get-cyber-alerts
    """
    next_page = response["currentPage"] + 1
    if next_page > response["totalPages"]:
        return {}
    return {
        "page": next_page
    }

# Extend the client for your API integration.
class NHSClient(APIClient):

    @paginated(by_query_params=get_next_page)
    @retry_request
    def get_all_cyberalerts(self, url: str) -> dict:
        return self.get(url)
