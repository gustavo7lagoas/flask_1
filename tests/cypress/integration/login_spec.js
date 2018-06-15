context('Login page', () => {
    beforeEach(() => {
        cy.visit('/login')
    })
    it('fails with invalid password', () => {
        cy.get('#username').type('ze das couves')
            .get('#passwd').type('invalid')
            .get('[data-cy="login"]').click()
            .get('.alert-danger')
            .should('contain', 'Invalid')
    })
    it('should redirect to list after login', () => {
        cy.get('#username').type('ze das couves')
            .get('#passwd').type('mestra')
            .get('[data-cy="login"]').click()
        cy.get('[data-cy="corpo-tabela"]')
            .should('exist')
    })
})
