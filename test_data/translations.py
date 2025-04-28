class Translations:
    DATA = {
        "en_US": {
            "title": "Reincorporation Delegations",
            "button": "Sign in with Google",
            "accessWithGoogle": "Access to reincorporation delegations",
            "firstNameMinError": "First name must be at least 3 characters long",
            "lastNameMinError": "Last name must be at least 3 characters long",
            "emailRequiredError": "Email is required",
            "headquarterError": "Please select a headquarter",
            "EditTitle": "Edit Reinstatement Responsible",
            "body": "Are you sure you want to save the changes?",
            "deleteAlertTitle": "Delete Reinstatement Responsible",
            "deleteBody": "Are you sure to delete the user"
        },
        "Español": {
            "title": "Responsables de Reincorporación",
            "button": "Accede con Google",
            "accessWithGoogle": "Acceso a delegaciones de reincorporación",
            "firstNameMinError": "El nombre debe tener al menos 3 caracteres",
            "lastNameMinError": "El apellido debe tener al menos 3 caracteres",
            "emailRequiredError": "El correo electrónico es requerido",
            "headquarterError": "Por favor seleccione una sede",
            "EditTitle": "Editar Responsable de Reincorporación",
            "body": "¿Está seguro de guardar los cambios?",
            "deleteAlertTitle": "Eliminar Responsable de Reincorporación",
            "deleteBody": "¿Está seguro de eliminar al usuario"
        },
        "pt_BR": {
            "title": "Delegações de Reincorporação",
            "button": "Entrar com o Google",
            "accessWithGoogle": "Acesso às delegações de reincorporação",
            "firstNameMinError": "O nome deve ter pelo menos 3 caracteres",
            "lastNameMinError": "O sobrenome deve ter pelo menos 3 caracteres",
            "emailRequiredError": "O email é obrigatório",
            "headquarterError": "Por favor, selecione uma sede",
            "EditTitle": "Editar o Responsável pela Reincorporação",
            "body": "Tem certeza de que deseja salvar as alterações?",
            "deleteAlertTitle": "Excluir o Responsável pela Reincorporação",
            "deleteBody": "Tem certeza de que deseja excluir o usuário"
        },
        "it_IT": {
            "title": "Delegazioni di Reincorporazione",
            "button": "Accedi con Google",
            "accessWithGoogle": "Accesso alle deleghe di reincorporazione",
            "firstNameMinError": "Il nome deve essere di almeno 3 caratteri",
            "lastNameMinError": "Il cognome deve essere di almeno 3 caratteri",
            "emailRequiredError": "L'email è obbligatoria",
            "headquarterError": "Seleziona una sede",
            "EditTitle": "Modifica il Responsabile della Reincorporazione",
            "body": "Sei sicuro di voler salvare le modifiche?",
            "deleteAlertTitle": "Elimina il Responsabile della Reincorporazione",
            "deleteBody": "Sei sicuro di voler eliminare l'utente"
        }
    }

    @classmethod
    def get_translation(cls, lang_code):
        return cls.DATA.get(lang_code, {})