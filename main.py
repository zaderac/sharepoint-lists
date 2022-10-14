from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

site_url = "https://rheindigital-my.sharepoint.com/personal/daniel_ehme_rheindigital_com"
ctx = ClientContext(site_url).with_credentials(UserCredential("daniel.ehme@rheindigital.com", "***"))

target_list = ctx.web.lists.get_by_title("Testlist2").get().execute_query()

print("List title: {0}".format(target_list.title))
