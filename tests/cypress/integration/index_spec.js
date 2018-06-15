context('Index', () => {
    it('Displays all games', () => {
        cy.visit('/')
            .get('[data-cy="corpo-tabela"] tr')
            .should('have.length', 4)
            .should('contain', 'Super Mario RPG')
    })
})
