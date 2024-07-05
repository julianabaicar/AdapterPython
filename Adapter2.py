class IUser:
    """
    Interface que define o comportamento esperado de todos os tipos de usuários.
    """

    def login(self, username: str, password: str) -> None:
        pass

    def get_permissions(self) -> list:
        pass


class Administrator(IUser):
    """
    Implementação concreta para o tipo de usuário Administrador.
    """

    def login(self, username: str, password: str) -> None:
        # Lógica de login para administrador
        pass

    def get_permissions(self) -> list:
        return ['cadastro_eventos', 'cadastro_usuarios', 'gerar_relatorios']


class Volunteer(IUser):
    """
    Implementação concreta para o tipo de usuário Voluntário.
    """

    def login(self, username: str, password: str) -> None:
        # Lógica de login para voluntário
        pass

    def get_permissions(self) -> list:
        return ['cadastro_eventos', 'visualizar_eventos']


class Beneficiary(IUser):
    """
    Implementação concreta para o tipo de usuário Beneficiário.
    """

    def login(self, username: str, password: str) -> None:
        # Lógica de login para beneficiário
        pass

    def get_permissions(self) -> list:
        return ['visualizar_eventos']


class BeneficiaryAdapter(IUser):
    """
    Adaptador para usuário Beneficiário que remove permissões de cadastro.
    """

    def __init__(self, beneficiary: Beneficiary):
        self.beneficiary = beneficiary

    def login(self, username: str, password: str) -> None:
        self.beneficiary.login(username, password)

    def get_permissions(self) -> list:
        permissions = self.beneficiary.get_permissions()
        permissions.remove('cadastro_eventos')
        permissions.remove('cadastro_usuarios')
        permissions.remove('gerar_relatorios')
        return permissions


def user_login(user: IUser, username: str, password: str) -> None:
    """
    Função que realiza o login do usuário e obtém suas permissões.
    """
    user.login(username, password)
    permissions = user.get_permissions()
    print(f"Usuário logado. Permissões: {permissions}")


if __name__ == "__main__":
    admin = Administrator()
    volunteer = Volunteer()
    beneficiary = Beneficiary()

    print("Login do administrador:")
    user_login(admin, "admin", "admin_pass")

    print("Login do voluntário:")
    user_login(volunteer, "volunteer", "volunteer_pass")

    print("Login do beneficiário (adaptado):")
    beneficiary_adapter = BeneficiaryAdapter(beneficiary)
    user_login(beneficiary_adapter, "beneficiary", "beneficiary_pass")
